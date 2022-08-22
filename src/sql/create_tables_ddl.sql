CREATE TABLE if not exists WEATHER
(station VARCHAR2(50),
row_date DATE,
min_temp NUMBER,
max_temp NUMBER,
amount NUMBER,
CONSTRAINT UC_record UNIQUE (station, row_date)
);

CREATE TABLE if not exists YIELD
(station VARCHAR2(50),
year VARCHAR2(4),
amount NUMBER,
CONSTRAINT UC_record UNIQUE (station, year)
);

CREATE TABLE if not exists  WEATHER_DATA_STATS
(station VARCHAR2(50),
year VARCHAR2(4),
avg_min_temp NUMBER,
avg_max_temp NUMBER,
total_amount NUMBER,
CONSTRAINT UC_record UNIQUE (station, year)
);
