insert into WEATHER_DATA_STATS
select station, strftime('%Y',row_date) as "Year",  avg(min_temp), avg(max_temp), sum(amount)
from WEATHER
where min_temp != -9999 and max_temp != -999 and amount != 9999
group by station, strftime('%Y',row_date)
;
