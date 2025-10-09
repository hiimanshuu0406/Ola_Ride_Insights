CREATE DATABASE OLA_project;
USE OLA_Project;

SELECT COUNT(*) FROM cleaned_ola_dataset;

SELECT * FROM cleaned_ola_dataset
LIMIT 10;

# 1. Retrieve all successful bookings
	SELECT *
	FROM cleaned_ola_dataset
	WHERE Booking_Status = 'Success';

	SELECT COUNT(*)
    FROM cleaned_ola_dataset
    WHERE Booking_Status = 'Success';
    
# 2. Find the average ride distance for each vehicle type
	SELECT Vehicle_Type, AVG(Ride_Distance) AS avg_distance
    FROM cleaned_ola_dataset
    WHERE Ride_Distance IS NOT NULL
    GROUP BY Vehicle_Type;
    
# 3. Get the total number of cancelled rides by customers:
	SELECT COUNT(*) AS rides_canceled_by_customers
    FROM cleaned_ola_dataset
    WHERE Booking_Status = 'Canceled by Customer';
    
# 4. List the top 5 customers who booked the highest number of rides:
	SELECT Customer_ID, COUNT(*) AS total_rides
    FROM cleaned_ola_dataset
    GROUP BY Customer_ID
    ORDER BY total_rides DESC
    LIMIT 5;
    
# 5. Get the number of rides cancelled by drivers due to personal and car-related issues:
	SELECT COUNT(*) AS Canceled_by_Driver_Personal_and_Car_Issue
    FROM cleaned_ola_dataset
    WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';
    
# 6. Find the maximum and minimum driver ratings for Prime Sedan bookings:
	SELECT MAX(Driver_Ratings) AS max_rating,
		   MIN(Driver_Ratings) AS min_rating
	FROM cleaned_ola_dataset
    WHERE Vehicle_Type = 'Prime Sedan'
		AND Driver_Ratings IS NOT NULL;

# 7. Retrieve all rides where payment was made using UPI:
	SELECT *
    FROM cleaned_ola_dataset
    WHERE Payment_Method = 'UPI';
    
	SELECT COUNT(*)
    FROM cleaned_ola_dataset
    WHERE Payment_Method = 'UPI';
    
# 8. Find the average customer rating per vehicle type:
	SELECT Vehicle_Type, AVG(Customer_Rating) AS avg_customer_rating
    FROM cleaned_ola_dataset
    WHERE Customer_Rating IS NOT NULL
    GROUP BY Vehicle_Type;
    
# 9. Calculate the total booking value of rides completed successfully:
	SELECT SUM(Booking_Value) AS Total_Value_of_Successful_Rides
    FROM cleaned_ola_dataset
    WHERE Booking_Status = 'Success';
    
# 10. List all incomplete rides along with the reason
	SELECT Booking_ID, Customer_ID, Vehicle_Type, Incomplete_Rides, Incomplete_Rides_Reason
    FROM cleaned_ola_dataset
    WHERE Incomplete_Rides = 'Yes';
    
	SELECT COUNT(*) AS incomplete_rides
    FROM cleaned_ola_dataset
    WHERE Incomplete_Rides = 'YES';