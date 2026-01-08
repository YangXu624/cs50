-- *** The Lost Letter ***

SELECT * FROM "scans"
WHERE "action" = 'Drop'
AND "package_id" = (
    SELECT "id" FROM "packages"
    WHERE "from_address_id" IN (
        -- nested query to find the address id FROM which the letter was sent
        SELECT "id" FROM "addresses"
        WHERE "address" = '900 Somerville Avenue'
    )
    AND "contents" LIKE '%Letter' -- found delivered address as 854
);

SELECT "address", "type" FROM "addresses"
WHERE "id" = '854'; -- 2 Finnigan Street

-- *** The Devious Delivery ***

SELECT * FROM "scans"
WHERE "action" = 'Drop'
AND "package_id" = (
    SELECT "id" FROM "packages" -- retrieve package id
    WHERE "contents" LIKE '%duck%' -- duck implied from written clues
    AND "from_address_id" IS NULL -- no "from address"
);

SELECT "contents" FROM "packages" -- retrieve package id
    WHERE "contents" LIKE '%duck%' -- duck implied from written clues
    AND "from_address_id" IS NULL;

SELECT "address", "type" FROM "addresses"
WHERE "id" = '348';

-- *** The Forgotten Gift ***

SELECT "contents" FROM "packages"
    WHERE "from_address_id" = (
        SELECT "id" FROM "addresses"
        WHERE "address" = '109 Tileston Street'
    );

SELECT * FROM "scans" s
JOIN "drivers" d
ON d."id" = s."driver_id"
WHERE s."package_id" = (
    SELECT "id" FROM "packages"
    WHERE "from_address_id" = (
        SELECT "id" FROM "addresses"
        WHERE "address" = '109 Tileston Street'
    )
);


