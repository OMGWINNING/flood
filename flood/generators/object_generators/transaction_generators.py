from __future__ import annotations

import typing

import flood
from flood import generators


def generate_transaction_hashes(
    n: int,
    network: str,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[str]:
    return generators.load_samples(
        network=network,
        datatype='transactions',
        n=n,
        random_seed=random_seed,
    )


def generate_uo_hashes(
    n: int,
    network: str,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[str]:
    return generators.load_json_samples(
        network=network,
        datatype='uo_hashes',
        n=n,
        random_seed=random_seed,
    )

def generate_uos_estimate(
    n: int,
    network: str,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[str]:
    return generators.load_json_samples(
        network=network,
        datatype='uos_estimate',
        filetype='uos',
        n=n,
        random_seed=random_seed,
    )

def generate_uos_sponsor(
    n: int,
    network: str,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[str]:
    return generators.load_json_samples(
        network=network,
        datatype='uos_sponsor',
        filetype='uos',
        n=n,
        random_seed=random_seed,
    )

def generate_uos_estimate_sponsor(
    n: int,
    network: str,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[str]:
    return generators.load_json_samples(
        network=network,
        datatype='uos_estimate_sponsor',
        filetype='uos',
        n=n,
        random_seed=random_seed,
    )
