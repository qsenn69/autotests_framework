from datetime import date, timedelta 

class Data: 
    
    def today() -> date: 
        return date.today() 
    
    def days_from_today(days: int) -> date: 
        return date.today() + timedelta(days=days) 
    
    def format_for_form(dt: date) -> str: 
        return dt.strftime("%d.%m.%Y") # 24.10.2024 
    
    def format_for_url(dt: date) -> str: 
        return dt.strftime("%d%m") #2410
    
    def get_formatted_range(start_offset: int, end_offset: int):
        
        start = Data.days_from_today(start_offset)
        end = Data.days_from_today(end_offset)
        return (
            Data.format_for_form(start),
            Data.format_for_form(end),
            Data.format_for_url(start),
            Data.format_for_url(end)
        )