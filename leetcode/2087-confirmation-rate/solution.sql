select user_id, round(avg(case when c.action = "confirmed" then 1 else 0 end),2) as confirmation_rate from Confirmations c right join Signups s using (user_id) group by 1;
