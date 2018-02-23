#1. Across all reservation partners for January & February, how many completed reservations occurred?
select sum(cnt) completed_reservations from (
select count(1) as cnt from club_ready_reservations crr where SIGNED_IN_AT IS NOT NULL and CANCELED = 0
UNION ALL
select count(1) as cnt from mbo_reservations mr  where CHECKED_IN_AT IS NOT NULL and CANCELED_AT IS NULL
) cr;
/*130*/

#2. Which studio has the highest rate of reservation abandonement (did not cancel but did not check-in)?
select studio_key, sum(cnt) from(
select studio_key, count(1) cnt from club_ready_reservations where canceled = 0 and signed_in_at is null group by studio_key
union all
select studio_key, count(1) cnt from mbo_reservations where canceled_at is null and checked_in_at is null group by studio_key) abandoned group by studio_key order by sum(cnt) desc;
#crossfit-control-jacksonville-beach	3
#orlando-yoga	3
#hive-athletics	3

#3. Which fitness area (i.e., tag) has the highest number of completed reservations for February
select class_tag, sum(cnt) from (
select class_tag, count(1) cnt from club_ready_reservations where date_key = '2018-02-01' and canceled = 0 and signed_in_at is not null group by class_tag 
union all
select class_tag, count(1) cnt from mbo_reservations where date_key = '2018-02-01' and canceled_at is null and checked_in_at is not null group by class_tag
) cr group by class_tag order by sum(cnt) desc;
#yoga	24

#4. How many members completed at least 1 reservation and had no more than 1 canceled reservation in January?
select count(distinct mr.member_id) cnt from
(select distinct member_id from club_ready_reservations where date_key = '2018-01-01' and RESERVED_FOR is not null
union all
select distinct member_id from mbo_reservations where date_key = '2018-01-01' and RESERVED_AT is not null) mr
where member_id not in
	(
		select member_id from mbo_reservations where date_key = '2018-01-01' and canceled_at IS NOT NULL group by member_id having count(1) > 1
        union all
        select member_id from club_ready_reservations where date_key = '2018-01-01' and canceled = 1 group by member_id having count(1) > 1
    ) ;
#24