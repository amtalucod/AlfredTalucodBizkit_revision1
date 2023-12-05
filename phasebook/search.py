from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    id = args.get("id")
    name = args.get("name")
    age = args.get("age")
    occupation = args.get("occupation")
    #variable for filtered users
    filteredUsers = []
    filteredIdUsers = []
    filteredNameUsers = []
    filteredAgeUsers = []
    filteredOccupationUsers = []

    if(id is None and name is None and age is None and occupation is None):
            filteredUsers = USERS
    else:        
        for user in USERS: 
            if (id is not None and id is not '' and id == user.get("id")):
                filteredIdUsers.append(user)
            else:
                if (name is not None and name is not '' and name.lower() in user.get("name").lower()):
                    idMatch = False
                    for filterUser in filteredIdUsers:                     
                        if (filterUser.get("id") == user.get("id")):
                            idMatch = True
                    if(idMatch==False):
                        filteredNameUsers.append(user)
                else:
                    if (age is not None and age is not '' and (int(age)-1) <= user.get("age") and (int(age)+1) >= user.get("age")):
                        idMatch = False
                        for filterUser in filteredIdUsers:                     
                            if (filterUser.get("id") == user.get("id")):
                                idMatch = True
                        for filterName in filteredNameUsers:                     
                            if (filterName.get("id") == user.get("id")):
                                idMatch = True
                        for filterAge in filteredAgeUsers:
                            if (filterAge.get("id") == user.get("id")):
                                idMatch = True
                        if(idMatch==False):
                            filteredAgeUsers.append(user)
                    else:
                        if (occupation is not None and occupation is not '' and occupation.lower() in user.get("occupation").lower()):
                            idMatch = False
                            for filterUser in filteredIdUsers:                     
                                if (filterUser.get("id") == user.get("id")):
                                    idMatch = True
                            for filterName in filteredNameUsers:                     
                                if (filterName.get("id") == user.get("id")):
                                    idMatch = True
                            for filterAge in filteredAgeUsers:
                                if (filterAge.get("id") == user.get("id")):
                                    idMatch = True
                            for filtered in filteredOccupationUsers:                     
                                if (filtered.get("id") == user.get("id")):
                                    idMatch = True
                            if(idMatch==False):
                                filteredOccupationUsers.append(user)
        
    filteredAgeUsers.extend(filteredOccupationUsers)
    filteredNameUsers.extend(filteredAgeUsers)
    filteredIdUsers.extend(filteredNameUsers)
    filteredUsers.extend(filteredIdUsers)

    return filteredUsers