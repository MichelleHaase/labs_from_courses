SELECT schools.name, staff_evaluations.unsatisfactory, graduation_rates.dropped FROM schools
    JOIN staff_evaluations ON schools.district_id = staff_evaluations.district_id
    JOIN graduation_rates ON schools.id = graduation_rates.school_id
    ORDER BY staff_evaluations.unsatisfactory DESC, graduation_rates.dropped DESC;
