
CREATE TABLE IF NOT EXISTS passengers (
    "id" INTEGER,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" INTEGER,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS airlines (
    "name" TEXT,
    "concourse" TEXT,
    PRIMARY KEY("name")
);

CREATE TABLE IF NOT EXISTS flights (
    "id" INTEGER,
    "flight_no" INTEGER,
    "airline" TEXT,
    "departing_code" TEXT,
    "arriving_code" TEXT,
    "departure_time" DATETIME,
    "arrival_time" DATETIME,
    PRIMARY KEY("id"),
    FOREIGN KEY("airline") REFERENCES "airlines"("name")
);

CREATE TABLE IF NOT EXISTS check_ins (
    "time" DATETIME,
    "passenger_id" INTEGER,
    "flight_id" INTEGER,
    FOREIGN KEY("passenger_id") REFERENCES "passengers"("id"),
    FOREIGN KEY("flight_id") REFERENCES "flights"("id")
);

