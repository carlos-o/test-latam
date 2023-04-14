import requests
import sys
# import redis

# CLIENT = redis.Redis(host='localhost', port=6379,  charset="utf-8", decode_responses=True)
# CACHE_TIME = 3600


class PropertyInformation:
    """
       A class used to represent a property

       ...

       Attributes
       ----------
       property_id : str
           id of property to find

       Methods
       -------
       _store_property_cache(property_info)
            store in redis the information of property
       _get_property_price_and_currency(property_data)
            parse information to get the price and currency of the property
       find_property()
            find in the graphql of infocasa for the information on price and  type of currency of specific property

       """
    def __init__(self, property_id: int):
        self.property_id = property_id

    # comment if you don't use docker
    # def _store_property_cache(self, property_info: dict) -> None:
    #     """
    #         store in redis the information of property
    #
    #         :param property_info: dict with price and currency of property
    #         :type property_info: dict
    #         :return: None
    #     """
    #     CLIENT.set(str(self.property_id), "{} {}".format(property_info.get('currency'), property_info.get('price')))
    #     CLIENT.expire(str(self.property_id), CACHE_TIME)
    #     return None
    # comment if you don't use docker

    def _get_property_price_and_currency(self, property_data: dict) -> dict:
        """
            parse information to get the price and currency of the property

            :param property_data: dict with information of property
            :type property_data: dict
            :return: dict with price and currency of property

        """
        if property_data.get('data').get('property') is None:
            print(f"Price not found for id {self.property_id}")
            sys.exit(1)
        data = property_data.get('data').get('property')
        return {"price": data.get('price').get('amount'), "currency": data.get('price').get('currency').get('name')}

    def find_property(self) -> None:
        """
            find in the graphql of infocasa for the information on price and  type of currency of specific property

            :return: None
        """
        url = 'https://graph.infocasas.com.uy/graphql'
        origin = 'www.infocasas.com.uy'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Origin': f'https://{origin}',
                   'x-origin': origin}
        # query to get price and currency of any property
        query = '''query property($id: ID!) {
            property(id: $id){
                id
                price {
                    amount
                    currency {
                        name
                    }
                }
            }
        }
        '''
        variables = {"id": self.property_id}
        try:
            response = requests.post(url=url, headers=headers, json={'query': query, 'variables': variables})
        except Exception as e:
            print(f"An error has occurred please try again {e}")
            sys.exit(1)

        if response.status_code == 200:
            property_info = self._get_property_price_and_currency(response.json())
            print(f"{property_info.get('currency')} {property_info.get('price')}")
            # comment if you don't use docker
            # self._store_property_cache(property_info)
            # comment if you don't use docker
        else:
            print(f"Price not found for id {self.property_id}")
            sys.exit(1)
        return None


def main():
    try:
        property_id = sys.argv[1]
    except IndexError as e:
        print('Please enter an input number')
        sys.exit(1)

    if property_id.isdigit():
        # check if property id exist in store
        # comment if you don't use docker
        # value = CLIENT.get(property_id)
        # if value:
        #     print(value)
        #     sys.exit(1)
        # comment if you don't use docker
        property_instance = PropertyInformation(property_id=int(property_id))
        property_instance.find_property()
    else:
        print('Please enter an input number')


if __name__ == '__main__':
    main()
