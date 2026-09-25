import streamlit as st

st.title("AI Traveller App")

Destination =st.text_input("Enter Destination:")
Travel_date=st.text_input("Enter Travel Date:")
budget=st.number_input("Enter Budget: ")

travel_type=st.selectbox(
    "Travel Type",
    ["Solo","Family","Couple","Business"]
    )

interest =st.multiselect(
    "Interest",
    ["Beach","Temple","Adventure","Nature"]
)

if st.button("Submit"):
    st.write("Budget Analysis")

    if budget < 10000:
      budget_category="Low Budget"
      hotel_type="Budget Hotel"

    elif budget< 30000:

      budget_category="Medium Budget"
      hotel_type="3-Star Hotel"

    elif budget < 60000:

      budget_category = "Premium Budget"
      hotel_type = "4-Star Hotel"

    else:

      budget_category="Luxury  Budget"
      hotel_type="5-Star Resort"

    st.write(f"Budget Category : {budget_category}")
    st.write(f"Recommended Stay : {hotel_type}")


    st.write("## Travel Recommendation")

    if travel_type == "Solo":
        st.info("Explore local attractions and backpacking routes.")

    elif travel_type == "Family":
        st.info("Choose family-friendly hotels and sightseeing packages.")

    elif travel_type == "Couple":
        st.info("Romantic resorts and candle-light dinners recommended.")

    elif travel_type == "Business":
        st.info("Stay near business districts with conference facilities.")

    score=0

    for item in interest:

      if item=="Adventure":
        score+=20   # score=score+20

      elif item=="Nature":
        score+=15

      else:
        score+=10

    if budget> 30000:
      score+=25

    if travel_type in ["Family","Couple"]:
      score+=25


    st.write(f"""
    ###Travel Summary

    Destination \t : {Destination}

    Travel Date \t : {Travel_date}

    Budgent \t : ₹{budget}

    Travel_type \t : {travel_type}

    Interst \t :{interest}

    Final Score: {score}

    """)

print("Thank you")
