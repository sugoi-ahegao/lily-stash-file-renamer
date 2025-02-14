from tests.testing_model_creators.create_scene import create_scene
from tests.testing_model_creators.create_stash_context import create_stash_context

from lily.filters.matches_stash_id import MatchesStashIDFilterSettings, matches_stash_id


class TestMatchesStashIdFilter:
    def test_scene_with_stash_id_passes(self):
        stash_ids = [{"stash_id": "some-stash-id", "endpoint": "some-endpoint"}]

        ctx = create_stash_context(scene=create_scene(stash_ids=stash_ids))
        assert matches_stash_id(ctx, MatchesStashIDFilterSettings(not_null=True)) is True

    def test_scene_with_no_stash_id_fails(self):
        ctx = create_stash_context(scene=create_scene(stash_ids=[]))
        assert matches_stash_id(ctx, MatchesStashIDFilterSettings(not_null=True)) is False

    def test_scene_with_stash_id_fails_if_should_have_stash_id_is_false(self):
        stash_ids = [{"stash_id": "some-stash-id", "endpoint": "some-endpoint"}]

        ctx = create_stash_context(scene=create_scene(stash_ids=stash_ids))
        assert matches_stash_id(ctx, MatchesStashIDFilterSettings(not_null=False)) is False

    def test_scene_with_no_stash_id_passes_if_should_have_stash_id_is_false(self):
        ctx = create_stash_context(scene=create_scene(stash_ids=[]))
        assert matches_stash_id(ctx, MatchesStashIDFilterSettings(not_null=False)) is True

    def test_scene_with_matching_stash_id_should_pass(self):
        stash_ids = [{"stash_id": "some-stash-id", "endpoint": "some-endpoint"}]

        ctx = create_stash_context(scene=create_scene(stash_ids=stash_ids))
        assert matches_stash_id(ctx, MatchesStashIDFilterSettings(value="some-stash-id")) is True
