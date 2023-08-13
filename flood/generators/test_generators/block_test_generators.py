from __future__ import annotations

import typing

from flood import spec
from flood.tests import load_tests
import flood

def generate_test_eth_supported_entry_points(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_supported_entry_points(
        n_calls=n_calls
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_eth_get_user_operation_by_hash(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_get_user_operation_by_hash(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_eth_get_user_operation_receipt(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_get_user_operation_receipt(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_eth_estimate_user_operation_gas(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_estimate_user_operation_gas(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_alchemy_request_paymaster_and_data(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_alchemy_request_paymaster_and_data(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_alchemy_request_gas_and_paymaster_and_data(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None, 
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_alchemy_request_gas_and_paymaster_and_data(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )

def generate_test_eth_get_block_by_number(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None,
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_get_block_by_number(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )


def generate_test_eth_fee_history(
    *,
    rates: typing.Sequence[int],
    duration: int | None = None,
    durations: typing.Sequence[int] | None = None,
    network: str,
    vegeta_args: flood.VegetaArgsShorthand | None = None,
    random_seed: spec.RandomSeed | None = None,
) -> typing.Sequence[flood.VegetaAttack]:
    n_calls = load_tests.estimate_call_count(
        rates=rates, duration=duration, durations=durations
    )
    calls = flood.generators.generate_calls_eth_fee_history(
        n_calls=n_calls,
        network=network,
        random_seed=random_seed,
    )
    return load_tests.create_load_test(
        calls=calls,
        rates=rates,
        duration=duration,
        durations=durations,
        vegeta_args=vegeta_args,
    )


# def generate_test_eth_get_block_by_hash(
#     *,
#     rates: typing.Sequence[int],
#     duration: int | None = None,
#     durations: typing.Sequence[int] | None = None,
#     network: str,
#     vegeta_args: typing.Mapping[str, str | None] | None = None,
#     random_seed: spec.RandomSeed | None = None,
# ) -> typing.Sequence[flood.VegetaAttack]:
#     n_calls = load_tests.estimate_call_count(
#         rates=rates, duration=duration, durations=durations
#     )
#     calls = flood.generate_calls_eth_get_block_by_hash(
#         n_calls=n_calls,
#         network=network,
#         random_seed=random_seed,
#     )
#     return load_tests.create_load_test(
#         calls=calls,
#         rates=rates,
#         duration=duration,
#         durations=durations,
        # vegeta_args=vegeta_args,
#     )
