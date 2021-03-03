
CREATE TABLE IF NOT EXISTS jgali3_assignment (
	sample_data jsonb NULL,
	load_timestamp timestamp NULL DEFAULT now(),
	load_timestamp_epoc int8 NULL DEFAULT date_part('epoch'::text, now())
);
