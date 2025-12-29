from DAL.UrlRepository import UrlRepository ## TODO for Docker Build Use this
#from _Test.ENV_Change_For_IDE_Base_Test.Expose_DB_For_IDE_Access_FronDocker import UrlRepository ## TODO for Container DB access To Use IDE with use this line
from Logic.Utils.Base62 import encode_base62
from Logic.Utils.Hashing import HashGen
from Models.UrlDto import ResponseDto

class UrlLogic:
    def __init__(self):
        self.DAL = UrlRepository()
        self.base_url = "http://localhost:8080/api/"

    def shorten_the_url_method(self, long_url):
        url_hash = HashGen(long_url)
        ## why do i check with a hash here
        ## Urls can be large and query for large content
        ## in db is not efficent when there is so many records in it
        ## so i added a hash gen to generate a hash from the url and
        ## use it to check if the record exists in db

        self.existing = self.DAL.get_by_url_hash(url_hash)
        if self.existing:
            short_code = self.existing['short_code']
            if short_code != None :
                return ResponseDto(
                    id=self.existing["id"],
                    short_code=short_code,
                    short_url=self.base_url + short_code,
                    long_url=self.existing["long_url"]
                )
        else:
            new_id = self.DAL.insert_new_url(long_url, url_hash)
            short_code = encode_base62(new_id)
            if len(short_code) > 5:
                raise ValueError("Short code exceeded max length of 5 characters")
            UpdateStatus = self.DAL.update_short_code(new_id, short_code)
            if UpdateStatus == None :
                record = self.DAL.get_by_id(new_id)
                if record :
                    return ResponseDto(
                        id=record["id"],
                        short_code=record["short_code"],
                        short_url=self.base_url + record["short_code"],
                        long_url=record["long_url"]
                    )
                else :
                    raise ValueError()
            else :
                return ResponseDto(
                    id=UpdateStatus["id"],
                    short_code=UpdateStatus["short_code"],
                    short_url=self.base_url + UpdateStatus["short_code"],
                    long_url=UpdateStatus["long_url"]
                )


    def get_long_url(self, short_code):
        record = self.DAL.get_by_short_code(short_code)
        if record:
            return record['long_url']
        return None