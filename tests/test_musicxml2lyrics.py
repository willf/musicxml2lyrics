from musicxml2lyrics.musicxml2lyrics import musicxml_to_lyrics


def test_musicxml_to_lyrics():
    assert musicxml_to_lyrics("foo") == "foo"
