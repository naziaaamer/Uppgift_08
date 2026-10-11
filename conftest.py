import pytest


@pytest.fixture
def context(context):
    context.set_default_timeout(10_000)
    return context
