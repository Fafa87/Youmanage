# Youmanage

Tools that allow you to easily manage the images, videos, sounds or other files that you have.

## Duplicates

One of the problems that I have is that there are multiple copies of the same photos in multiple places and when I want to integrate there is always a question - did I already downloaded those photos and stored them in some folder?

That's where this tools comes in. It can:
- calculate two-hashes of all files and then use that to determine the duplicates between different root dirs

### Usage

You can always check out available functions and help:

`python -m find_duplicates`

Prepare hashionary json for the given root:

`python -m find_duplicates prepare_hashionary --root_dir "C:\Users\Fafa\Desktop\Karty SD\4GB SD" --save_path "C:\Users\Fafa\Desktop\Karty SD\4GB SD.json"`

Check new root vs the already created hashionary:

`python -m find_duplicates check_against_base --new_root D:\Fafa\MyResources\data\new_photos --base_path "C:\Users\Fafa\Desktop\Karty SD\4GB SD.json"`