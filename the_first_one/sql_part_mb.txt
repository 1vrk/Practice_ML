set @select_columns = (
    select group_concat(
        concat(
            column_name, ', ',
            'lag(', column_name, ', 1) over w as ', column_name, '_1, ',
            'lag(', column_name, ', 2) over w as ', column_name, '_2'
        )
        SEPARATOR ',\n    '
    )
    from information_schema.columns information_schema
    where table_name = 'data_prep_rdy' and column_name not in ('client_id', 'segm_date')
    order by ordinal_position
);

select length(@select_columns);
set group_concat_max_len = 1000000;

set @full_query = concat(
'with prepared_data as (
    select *
    from data_prep_rdy
)
select client_id, segm_date,', @select_columns, '
from prepared_data
window w as (partition by client_id)'
);

prepare stmt
from @full_query;
execute stmt;
deallocate prepare stmt;