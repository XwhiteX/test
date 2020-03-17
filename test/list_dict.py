import sys
def test1(
        recorderId=None,
        uid=None,
        x=None,
        y=None,
        # region=None,
        regionCount=None,
        user_list=None):
    # region = [{
    #     "uid": uid,
    #     "x": x,
    #     "y": y
    # }]
    # region =  region_list

    info_dict = {
        "recorderId": recorderId,
        "regionCount": regionCount,
        "region_list": user_list
    }
    print(info_dict)
    return info_dict

uid = ''
x = ''
y = ''
input_regionCount = input('please input regionCount: ')
regionCount = int(input_regionCount)
user = []
if regionCount == 1:
    user = [{'uid': 1, 'x': 1, 'y': 1}]
    a = test1(recorderId=1, regionCount=regionCount, user_list=user)
elif regionCount == 2:
    user = [{'uid': 1, 'x': 1, 'y': 1}, {'uid': 2, 'x': 2, 'y': 2}]
    a = test1(recorderId=1, regionCount=regionCount, user_list=user)
