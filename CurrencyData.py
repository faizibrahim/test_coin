import datetime
import requests
import traceback


class CurrencyData(object):
    url = "https://graphs.coinmarketcap.com/currencies/{coin}/{start}/{end}/"

    def __init__(self, coin=None, beg_time=None, end_time=None):
        self.params = dict()
        if coin:
            self.params['coin'] = coin
        else:
            (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
            self.params['coin'] = text[:text.find('=')].strip()
        if beg_time:
            self.beg_time(beg_time)
        else:
            self.beg_time(datetime.datetime.now() - datetime.timedelta(hours=2))
        if end_time:
            self.end_time(end_time)
        else:
            self.end_time(datetime.datetime.now())
        self.data = None

    @staticmethod
    def _parse_time_for_site(stime):
        if isinstance(stime, datetime.datetime):
            result = str((stime-datetime.datetime(1970,1,1)).total_seconds()).split('.')[0] + '000'
        else:
            result = str((datetime.datetime.strptime(stime, "%m/%d/%Y-%H:%M:%S")-datetime.datetime(1970,1,1)).total_seconds()).split('.')[0] + '000'
        return result

    def _retrieve_data(self):
        response = requests.get(CurrencyData.url.format(**self.params))
        self.data = response.json()["price_usd"]

    def get_data(self,start_time=None,end_time=None):
        if start_time: self.beg_time(start_time)
        if end_time: self.end_time(end_time)
        self._retrieve_data()
        return self.data

    def get_data_for_last_hour(self):
        self.beg_time(datetime.datetime.now()-datetime.timedelta(hours=1))
        self.end_time()
        return self.get_data()

    def beg_time(self, time):
        self.params['start'] = self._parse_time_for_site(time)

    def end_time(self, time=None):
        self.params['end'] = self._parse_time_for_site(time) if time else self._parse_time_for_site(datetime.datetime.now())