"""
    Avatar Generator
    Author: Luiz Marin

    Generate random avatars from different parts.

    USAGE:  python app.py PARAM
            --help  ->  Display help
            all     ->  Generate all possible combinations
            random  ->  Generate random avatar

    Assets need to be in an specific name style

        BG0x.png    -   Background
        SK0x.png    -   Skin
        EY0x.png    -   Eyes
        MO0x.png    -   Mouth

    Set the correct paths and image size before running!
"""
from PIL import Image
import hashlib
import os
import random
import sys


# ---------- CONSTANTS -------------
# Define Image Size
IMAGE_SIZE = 25

# Define main paths
ASSETS_PATH = "./assets/"
RANDOM_PATH = "./random/"
ALL_PATH = "./all/"
#-----------------------------------


# Prepare lists
bgs = []
skins = []
eyes = []
mouths = []


# Help string
HELP = f"Usage: python {sys.argv[0]} [--help] | all random]"

def load_assets(path):
    """ Search and load assets from the path provided

        Parameters      :       path
    """

    with os.scandir(ASSETS_PATH) as assets:
        for entry in assets:
            if not entry.name.startswith('.') and entry.is_file():

                # Get first character and look for a match in the folder
                char = entry.name[0]
                if char == "B":
                    bgs.append(Image.open(ASSETS_PATH+entry.name))
                elif char == "S":
                    skins.append(Image.open(ASSETS_PATH+entry.name))
                elif char == "E":
                    eyes.append(Image.open(ASSETS_PATH+entry.name))
                elif char == "M":
                    mouths.append(Image.open(ASSETS_PATH+entry.name))
                else:
                    print("Assets not found in the "+ASSETS_PATH+" folder!")
    

def hash_file(file_name):
    """ Return the SHA1 hash from a given file

        Parameters      :       file_name

        Return          :       hash
    """

    BUFFER_SIZE = 1024

    hash = hashlib.sha1()

    # Open file and read in binary mode
    with open(file_name,'rb') as file:

        # Loop through the file
        chunk = 0
        while chunk != b'':
            chunk = file.read(BUFFER_SIZE)
            hash.update(chunk)

    # Return digested hash
    return hash.hexdigest()


def generate_all():
    """ Generate all possible combinations of avatars

        Parameters      :       None

        Return          :       None
    """

    for skin in skins:
        sk_i = str(skins.index(skin)+1)
        for eye in eyes:
            ey_i = str(eyes.index(eye)+1)
            for mouth in mouths:
                mo_i = str(mouths.index(mouth)+1)
                for bg in bgs:
                    bg_i = str(bgs.index(bg)+1)

                    avatar = Image.new("RGBA", (IMAGE_SIZE,IMAGE_SIZE))

                    avatar.paste(bg, bg.convert('RGBA'))
                    avatar.paste(skin,skin.convert('RGBA'))
                    avatar.paste(eye,eye.convert('RGBA'))
                    avatar.paste(mouth,mouth.convert('RGBA'))

                    avatar.save(ALL_PATH+"avatar_"+sk_i+ey_i+mo_i+bg_i+".png", format='png')

                    del avatar


def randomize():
    """ Generate a random avatar

        Parameters      :       None

        Return          :       None
    """

    avatar = Image.new("RGBA", (IMAGE_SIZE,IMAGE_SIZE))

    bg_i = random.randrange(0,len(bgs))
    avatar.paste(bgs[bg_i], bgs[bg_i].convert('RGBA'))

    skin_i = random.randrange(0,len(skins))
    avatar.paste(skins[skin_i],skins[skin_i].convert('RGBA'))

    eye_i = random.randrange(0,len(eyes))
    avatar.paste(eyes[eye_i],eyes[eye_i].convert('RGBA'))

    mouth_i = random.randrange(0,len(mouths))
    avatar.paste(mouths[mouth_i],mouths[mouth_i].convert('RGBA'))

    # 
    avatar.save(RANDOM_PATH+"avatar_random.tmp", format='png')

    # Calculate hash from the file
    hash = hash_file(RANDOM_PATH+"avatar_random.tmp")
    print("Random avatar created with SHA-1: "+hash)

    os.rename(RANDOM_PATH+"avatar_random.tmp", "./random/avatar_"+hash+".png")


def main():
    """ Main function, parse args and execute 
    """
    args = sys.argv[1:]

    if not args:
        raise SystemExit(HELP)

    if args[0] == "--help":
        print(HELP)
    elif args[0] == "all":
        print("Generating all possible combinations...")
        generate_all()
    elif args[0] == "random":
        print("Generating random avatar...")
        randomize()


if __name__ == '__main__':
    load_assets(ASSETS_PATH)
    main()