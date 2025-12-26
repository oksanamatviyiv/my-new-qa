import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 57
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emojis_not_empty(github_api):
    emojis = github_api.get_emojis()
    assert isinstance(emojis, dict)
    assert len(emojis) > 0


@pytest.mark.api
def test_specific_emoji_exists(github_api):
    emojis = github_api.get_emojis()
    assert "smile" in emojis


@pytest.mark.api
def test_non_existent_emoji_does_not_exist(github_api):
    emojis = github_api.get_emojis()
    assert "heartttt" not in emojis


@pytest.mark.api
def test_commits_list_not_empty(github_api):
    commits = github_api.list_commits("oksanamatviyiv", "my-new-qa")
    assert isinstance(commits, list)
    assert len(commits) > 0


@pytest.mark.api
def test_last_commit_has_author(github_api):
    commits = github_api.list_commits("oksanamatviyiv", "my-new-qa")
    last_commit = commits[0]
    info = last_commit["commit"]
    assert "author" in info
    assert "name" in info["author"]
    assert "date" in info["author"]
