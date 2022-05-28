import random


def throw_dice(dice_code):
    dice = dice_decode(dice_code)
    if dice is None:
        print("Dice Code incorrect")
        return None

    throws = dice['throws']
    sides = dice['sides']
    result = dice['modifier']

    for i in range(throws):
        result += random.randint(1, sides)

    return result


def dice_decode(dice_code):
    # Check if "D" is present in the code
    if not dice_code.count("D"):
        print("Incorrect die code - no 'D' found")
        return None
    # Set the default die dictionary
    die = {'throws': 1, 'sides': 6, 'modifier': 0}

    # Check if numer of throws is greater than one
    if dice_code[0] != 'D':
        try:
            die['throws'] = int(str(dice_code).split('D')[0])
        except ValueError:
            print("Incorrect throw number format")
            return None
        dice_code = str(dice_code).split('D')[1]
    else:
        dice_code = dice_code.replace('D', '')

    # Check if modifier is present in the code and distribute data to appropriate dictionary fields
    if dice_code.count('-'):
        try:
            die['modifier'] = int(str(dice_code.split('-')[1])) * -1
        except ValueError:
            print("Incorrect modifier format")
            return None
        try:
            die['sides'] = int(str(dice_code.split('-')[0]))
        except ValueError:
            print("Incorrect sides number format")
            return None
    elif dice_code.count('+'):
        try:
            die['modifier'] = int(str(dice_code.split('+')[1]))
        except ValueError:
            print("Incorrect modifier format")
            return None
        try:
            die['sides'] = int(str(dice_code.split('+')[0]))
        except ValueError:
            print("Incorrect sides number format")
            return None
    else:
        try:
            die['sides'] = int(dice_code)
        except ValueError:
            print("Incorrect side number format")
            return None

    # Check if the Die type is within the list of allowed Dice types
    allowed_dice = (3, 4, 6, 8, 10, 12, 20, 100)
    if die['sides'] not in allowed_dice:
        print(f"D{die['sides']} die is not allowed")
        return None
    return die


# dice_decode("2D10+10")
#print(throw_dice("4D100+1"))
