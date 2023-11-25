from PIL import Image
import argparse

def crop(filename:str, xOffset:int, yOffset:int, width:int, height:int, numX:int, numY:int, gapX:int=0, gapY:int=0):
    """
    Crop a tileset into individual tiles
    filename: The filename of the tileset to crop
    xOffset: The x offset of the first tile
    yOffset: The y offset of the first tile
    width: The width of the tiles
    height: The height of the tiles
    numX: The number of tiles in the x direction
    numY: The number of tiles in the y direction
    gapX: The gap between each tile in the x direction
    gapY: The gap between each tile in the y direction
    """
    img = Image.open(filename)
    iterations =0
    for x in range(xOffset, width*numX+xOffset, width+gapX):
        for y in range(yOffset, height*numY+yOffset , height+gapY):
            area = (x, y, x+width, y+height)
            cropped_img = img.crop(area)
            cropped_img.save(f'out/{remove_extnesion(filename)}_{iterations}.png')
            iterations += 1 

def remove_extnesion(filename:str):
    """
    Remove the extension from a filename
    filename: The filename to remove the extension from
    """
    return filename.split('.')[0]

parser = argparse.ArgumentParser(description="Crop a tileset into individual tiles")
parser.add_argument('-f', '--filename', type=str, default=None, help="The filename of the tileset to crop", required=True)
parser.add_argument('-w', '--width', type=int, default=32, help="The width of the tiles")
parser.add_argument('-hi', '--height', type=int, default=32, help="The height of the tiles")
parser.add_argument('-x', '--xoffset', type=int, default=0, help="The x offset of the first tile")
parser.add_argument('-y', '--yoffset', type=int, default=0, help="The y offset of the first tile")
parser.add_argument('-nx', '--numx', type=int, default=1, help="The number of tiles in the x direction")
parser.add_argument('-ny', '--numy', type=int, default=1, help="The number of tiles in the y direction")
parser.add_argument('-gx', '--gapx', type=int, default=0, help="The gap between each tile in the x direction")
parser.add_argument('-gy', '--gapy', type=int, default=0, help="The gap between each tile in the y direction")

if __name__ == "__main__":
    args = parser.parse_args()
    crop(args.filename, args.xoffset, args.yoffset, args.width, args.height, args.numx, args.numy, args.gapx, args.gapy)
    print(f"Successfully cropped {args.numx*args.numy} tiles")