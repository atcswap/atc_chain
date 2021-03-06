import pytest

from atc_chain.state.crosslink_record import (
    CrosslinkRecord,
)


@pytest.mark.parametrize(
    'param,default_value',
    [
        ('dynasty', 0),
        ('slot', 0),
        ('hash', b'\x00'*32),
    ]
)
def test_defaults(param, default_value, sample_crosslink_record_params):
    del sample_crosslink_record_params[param]
    crosslink = CrosslinkRecord(**sample_crosslink_record_params)

    assert getattr(crosslink, param) == default_value
