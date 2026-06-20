from quill.setup.versions import V1

def install():
    v1 = V1(__file__)
    v1.copy("wizard.py")
    v1.copy("package.json")

    v1.bins([
        "_/bin/tinker",
        "_/bin/tinker.cmd",
    ])

    v1.copy("bin/")

def uninstall():
    v1 = V1(__file__)
    v1.delete("wizard.py")
    v1.delete("package.json")

    v1.delete("@/bin/tinker")
    v1.delete("@/bin/tinker.cmd")

    v1.delete("bin/")
