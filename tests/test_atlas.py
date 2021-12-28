from nightroute import NightRouteAtlas, ObservationPoint


def test_format_story_empty():
    atlas = NightRouteAtlas()
    assert atlas.format_story() == "No points logged yet."


def test_format_story_with_points():
    atlas = NightRouteAtlas()
    atlas.add_point(ObservationPoint(name="River Watch", city="Emberfield", brightness=7))
    atlas.add_point(ObservationPoint(name="Lantern Line", city="Lumen Ridge", brightness=4))

    story = atlas.format_story()
    assert "River Watch" in story
    assert "Lumen Ridge" in story
    assert story.count("\n") == 1
