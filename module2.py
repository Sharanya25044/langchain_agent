# -------------------------------
# Tool Abstraction
# -------------------------------

class Tool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description

    def run(self, input):
        try:
            return self.func(input)
        except Exception as e:
            return f"Tool Error: {str(e)}"


# -------------------------------
# Calculator Tool (5 calculations)
# -------------------------------

def calculator(expression):

    try:

        if "+" in expression:
            a, b = expression.split("+")
            result = float(a) + float(b)

        elif "-" in expression:
            a, b = expression.split("-")
            result = float(a) - float(b)

        elif "*" in expression:
            a, b = expression.split("*")
            result = float(a) * float(b)

        elif "/" in expression:
            a, b = expression.split("/")
            b = float(b)

            if b == 0:
                return "Error: Division by zero"

            result = float(a) / b

        elif "^" in expression:
            a, b = expression.split("^")
            result = float(a) ** float(b)

        else:
            return "Unsupported calculation"

        return f"Result: {result}"

    except ValueError:
        return "Error: Invalid numbers"

    except Exception as e:
        return f"Calculation Error: {str(e)}"


# -------------------------------
# Weather Tool (Mock API)
# -------------------------------

def weather(city):

    fake_weather_db = {
    "New Delhi": "36°C, Partly Cloudy",
    "Mumbai": "42°C, Sunny (Heatwave)",
    "Bengaluru": "31°C, Partly Cloudy",
    "Hyderabad": "33°C, Sunny",
    "Chennai": "33°C, Humid",
    "Kolkata": "31°C, Clear",
    "Lucknow": "33°C, Warm",
    "Jaipur": "36°C, Dry",
    "Patna": "33°C, Thunderstorm Alert",
    "Bhopal": "37°C, Sunny"
}

    return fake_weather_db.get(city, "Weather data unavailable")


# -------------------------------
# Create Tools
# -------------------------------

calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Performs math calculations like addition, subtraction, multiplication, division and power"
)

weather_tool = Tool(
    name="WeatherAPI",
    func=weather,
    description="Returns weather information for a city"
)

tools = {
    "calculator": calculator_tool,
    "weather": weather_tool
}


# -------------------------------
# Fake Agent
# -------------------------------

class FakeAgent:

    def __init__(self, tools):
        self.tools = tools

    def invoke(self, query):

        print("\nQuestion:", query)

        response = ""

        # Detect math query
        if "+" in query or "-" in query or "*" in query or "/" in query or "^" in query:

            print("Thought: I need to calculate something")

            expr = ""
            for word in query.split():
                if "+" in word or "-" in word or "*" in word or "/" in word or "^" in word:
                    expr = word

            print("Action: Calculator")
            print("Action Input:", expr)

            result = self.tools["calculator"].run(expr)

            print("Observation:", result)
            response += result + "\n"

        # Detect weather query
        if "weather" in query.lower():

            print("Thought: I need weather information")

            city = query.split()[-1]

            print("Action: WeatherAPI")
            print("Action Input:", city)

            result = self.tools["weather"].run(city)

            print("Observation:", result)
            response += f"Weather in {city}: {result}"

        print("\nFinal Answer:")
        print(response)


# -------------------------------
# Run Agent
# -------------------------------

agent = FakeAgent(tools)

while True:

    user_query = input("\nAsk something (type 'exit' to stop): ")

    if user_query.lower() == "exit":
        break

    agent.invoke(user_query)
