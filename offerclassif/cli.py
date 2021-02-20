import json

import numpy as np
import typer
from joblib import load, dump

from offerclassif.data import get_df, load_json
from offerclassif.embedding import get_vectors
from offerclassif.utils import P, format_prediction

from sklearn.ensemble import ExtraTreesClassifier

app = typer.Typer()


@app.command()
def train(sample_file:str, thesaurus_file:str, output_file:str):

    typer.secho(f"Loading job thesaurus from {thesaurus_file} ...", fg=typer.colors.GREEN)
    thesaurus = load_json(thesaurus_file)

    typer.secho(f"Loading training samples from {sample_file} ...", fg=typer.colors.GREEN)
    data = load_json(sample_file)
    df = get_df(data, thesaurus)
    X = get_vectors(df.title)

    typer.secho("Training models ...", fg=typer.colors.GREEN)
    et_sect = ExtraTreesClassifier(oob_score=True, bootstrap=True, n_estimators=1000, random_state=1) 
    et_sect.fit(X, df.sector_internal_label)

    new_X = np.hstack([X, et_sect.oob_decision_function_])

    et_lib = ExtraTreesClassifier(oob_score=True, bootstrap=True, n_estimators=1000, random_state=1) 
    et_lib.fit(new_X, df.internal_label)
    
    typer.secho(f"Saving model to {output_file} ...", fg=typer.colors.GREEN)
    dump((et_sect, et_lib), output_file)


@app.command()
def predict(sample_file:str, thesaurus_file:str, model:str, output_file:str=None):
    typer.secho("Loading sklearn models ...", fg=typer.colors.GREEN)
    et_sect, et_lib = load(model)

    typer.secho(f"Loading job thesaurus from {thesaurus_file} ...", fg=typer.colors.GREEN)
    thesaurus = load_json(thesaurus_file)

    typer.secho(f"Loading samples from {sample_file} ...", fg=typer.colors.GREEN)
    data = load_json(sample_file)
    df = get_df(data)
    X = get_vectors(df.title)

    typer.secho(f"Making predictions ...", fg=typer.colors.GREEN)
    pred_sect = et_sect.predict_proba(X)
    X_new = np.hstack([X, pred_sect])
    pred = et_lib.predict(X_new)

    if output_file:
        typer.secho(f"Saving prediciton to {output_file} ...", fg=typer.colors.GREEN)
        format_prediction(data, pred, thesaurus)
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
    else:

        typer.secho("Results:", fg=typer.colors.MAGENTA)
        
        for i,j in zip(data, pred):
            typer.echo("")
            typer.echo(f"   id:             {i['_id']}")
            typer.echo(f"   title:          {i['title']}")
            typer.echo(f"   description:    {i['description'][:70]}...")
            typer.echo(f"   internal_label: " + typer.style(j, fg=typer.colors.GREEN))

        typer.echo("")


if __name__ == "__main__":
    app()