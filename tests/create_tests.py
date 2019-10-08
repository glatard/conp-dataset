from string import Template
from git import Repo


submodules = list(map(lambda x: x.name, Repo(".").submodules))

template = Template("""from functions import examine


def test_$clean_title():
    assert examine('$path') == 'All good'
""")

for dataset in submodules:
    with open("tests/test_" + dataset.replace("/", "_") + ".py", "w") as f:

        f.write(template.substitute(path=dataset,
                                    clean_title=dataset.replace("/", "_").replace("-", "_")))
