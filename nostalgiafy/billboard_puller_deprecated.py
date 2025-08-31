import nostalgia_years
import billboard
import personality_quiz

years_list = nostalgia_years.nostalgia_years_generator()

def chart_puller():
    chart = billboard.ChartData('hot-100', year=2024)
    return chart

print(chart_puller())