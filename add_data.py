from glob import glob

files = glob('md_disease/*')
for f in files:
    with open(f) as md:
        content = md.read()

        Post(
            title =f.split('/')[-1],
            content=content,
            username='admin2'
        )