/************************************************************
    INSERT users
*************************************************************/

INSERT INTO users (email, username, password)
VALUES ('joe@email.com', 'joe_39939', '9e93i3j88d'),
       ('jane@email.com', 'jane_773', 'k29w7h347e'),
       ('bill@email.com', 'bill_029', 'i782hbf67g'),
       ('sue@email.com', 'sue_54351', '.3;3;30877'),
       ('ted@email.com', 'ted_23423', ';po09ioo99'),
       ('tim@email.com', 'tim987989', '0aao0rg9ki'),
       ('frank@email.com', 'frank_0', 'i782hbf67g'),
       ('sheryl@email.com', 'sheryl', '.3;3;30877'),
       ('alice@email.com', 'alice44', ';po09ioo99'),
       ('jim@email.com', 'jim980089', '0aao0rg9ki');


/************************************************************
    INSERT vehicles
*************************************************************/

INSERT INTO vehicles (year, make, model, engine)
VALUES (1996, 'Ford', 'Taurus', '3.0L'),
       (2000, 'Honda', 'S2000', '2.0L'),
       (1957, 'Chevrolet', 'Bel Air', '5.7L'),
       (2006, 'BMW', '330xi', '3.0L'),
       (2020, 'Nissan', 'Altima', '2.4L'),
       (2003, 'Mercury', 'Cougar', '2.5L'),
       (2011, 'Toyota', 'Tacoma', '4.0L'),
       (2019, 'Chrysler', '300', '3.5L'),
       (1999, 'Plymouth', 'Voyager', '3.3L'),
       (2000, 'Mercedes-Benz', 'E320', '3.2L');


/************************************************************
    INSERT posts
*************************************************************/

INSERT INTO posts (title, repair_steps, user_id, vehicle_id)
VALUES ('Auxiliary Cooling Fan', '[{"test":"testing"}]', 1, 1),
       ('Alternator', '[{"test":"testing"}]', 2, 2),
       ('Starter', '[{"test":"testing"}]', 3, 3),
       ('Radiator', '[{"test":"testing"}]', 4, 4),
       ('Oil Change', '[{"test":"testing"}]', 5, 5),
       ('Drive Belt', '[{"test":"testing"}]', 6, 6),
       ('Intake Manifold', '[{"test":"testing"}]', 7, 7),
       ('Engine Mounts', '[{"test":"testing"}]', 8, 8),
       ('Front Brakes', '[{"test":"testing"}]', 9, 9),
       ('Tail Light Bulb', '[{"test":"testing"}]', 10, 10);


/************************************************************
    INSERT: tags
*************************************************************/

INSERT INTO tags (tag) VALUES ('alternator') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (11,
    (SELECT id FROM tags WHERE tag = 'alternator'));

INSERT INTO tags (tag) VALUES ('90A') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (12,
    (SELECT id FROM tags WHERE tag = '90A'));

INSERT INTO tags (tag) VALUES ('denso') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (13,
    (SELECT id FROM tags WHERE tag = 'denso'));

INSERT INTO tags (tag) VALUES ('starter') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (14,
    (SELECT id FROM tags WHERE tag = 'starter'));

INSERT INTO tags (tag) VALUES ('N52') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (15,
    (SELECT id FROM tags WHERE tag = 'N52'));

INSERT INTO tags (tag) VALUES ('VIN 5') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (16,
    (SELECT id FROM tags WHERE tag = 'VIN 5'));

INSERT INTO tags (tag) VALUES ('radiator') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (17,
    (SELECT id FROM tags WHERE tag = 'radiator'));

INSERT INTO tags (tag) VALUES ('belt') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (18,
    (SELECT id FROM tags WHERE tag = 'belt'));

INSERT INTO tags (tag) VALUES ('air filter') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (19,
    (SELECT id FROM tags WHERE tag = 'air filter'));

INSERT INTO tags (tag) VALUES ('sunroof') ON CONFLICT DO NOTHING;
INSERT INTO posts_tags (post_id, tag_id) VALUES (20,
    (SELECT id FROM tags WHERE tag = 'sunroof'));



/************************************************************
    INSERT comments
*************************************************************/

INSERT INTO comments (comment, post_id, user_id)
VALUES ('Cool post dude!', 20, 1),
       ('Nice job.', 11, 2),
       ('Thanks for posting', 12, 3),
       ('I like this approach', 13, 4),
       ('Never thought of that before', 14, 5),
       ('What tool are you using in step 5?', 15, 6),
       ('How long does this take?', 16, 7),
       ('Super cool', 17, 8),
       ('This confuses me', 18, 9),
       ('Be careful', 19, 10);
