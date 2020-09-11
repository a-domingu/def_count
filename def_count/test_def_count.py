import os, shutil
import git, pytest
from pyspark import SparkContext
from def_count import get_files, count

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    From https://stackoverflow.com/a/2656405

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise Exception("Cannot delete dir with shutil.rmtree")


@pytest.fixture
def workspace():
    path = os.path.join(os.getcwd(), '__downloaded__')
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        git.Repo.clone_from('https://github.com/a-domingu/download_repos', path, depth = 1)
    except Exception:
        pass
    yield path
    try:
        shutil.rmtree(path, onerror=onerror)
    except Exception as ex:
        print(ex)

def test_get_files(workspace):
    assert len(get_files(workspace)) == 3
    assert os.path.join(os.getcwd(), '__downloaded__', 'get_repos', 'repos.py') in get_files(workspace)

def test_count(workspace):
    ls_files = get_files(workspace)
    num = count(ls_files)
    assert num == 11




