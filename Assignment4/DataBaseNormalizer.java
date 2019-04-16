
import java.sql.*;


public class DataBaseNormalizer {
    Connection connect = SQLDatabaseConnection.getdatabaseconnection();

    public void TableCreation() throws SQLException{


        //This was a test table to make sure everything was storing correctly
        PreparedStatement PeopleTable = connect.prepareStatement("Create Table IF NOT EXISTS PeopleInfo (" +
                "PersonName VARCHAR(50)," +
                "Job VARCHAR(50)," +
                "PhoneNumber VARCHAR (50)," +
                "State VARCHAR (50)," +
                "Zipcode VARCHAR(50)," +
                "StreetName VARCHAR(50)," +
                "BuildingNumber VARCHAR(50)," +
                "City VARCHAR(50)," +
                "CreditCard VARCHAR(50)," +
                "CreditProvider VARCHAR(50)," +
                "SocialSecurityNumber VARCHAR(50));");
        PeopleTable.executeUpdate();

        //Creating a composite key
        PreparedStatement ssnPersonKey = connect.prepareStatement("CREATE TABLE IF NOT EXISTS ssnPersonKey(" +
                "PersonaName VARCHAR(50)," +
                "SocialSecurityNumber VARCHAR(50))");
        ssnPersonKey.executeUpdate();

        //Person information key
        PreparedStatement personInfo = connect.prepareStatement("CREATE TABLE IF NOT EXISTS personInfo(" +
                "PersonName VARCHAR(50)," +
                "Job VARCHAR(50)," +
                "PhoneNumber VARCHAR(50)," +
                "Zipcode VARCHAR(50)," +
                "BuildingNumber VARCHAR(50)," +
                "StreetName VARCHAR(50)," +
                "CreditCard VARCHAR(50))");
        personInfo.executeUpdate();

        //Zipcode and city
        PreparedStatement zipCity = connect.prepareStatement("CREATE TABLE IF NOT EXISTS zipCity(" +
                "Zipcode VARCHAR(50)," +
                "City VARCHAR(50))");
        zipCity.executeUpdate();


        //City information
        PreparedStatement cityInfo = connect.prepareStatement("CREATE TABLE IF NOT EXISTS cityInfo(" +
                "City VARCHAR(50)," +
                "State VARCHAR(50))");
        cityInfo.executeUpdate();

        //Credit Card Information
        PreparedStatement creditCardInfo = connect.prepareStatement("CREATE TABLE IF NOT EXISTS creditCardInfoCompany(" +
                "CreditCard VARCHAR(50)," +
                "CreditCardProvider VARCHAR(50))");
        creditCardInfo.executeUpdate();

    }


    //Inserting into composite key
    public String ssnPersonKey(String name, String socialSecurity) throws SQLException {
        //Composit Key
        CSVReader CSVData = new CSVReader();


        PreparedStatement InsertTable = connect.prepareStatement("INSERT INTO ssnPersonKey(PersonaName,SocialSecurityNumber)" +
                "VALUES(?,?)");
        InsertTable.setString(1, name);
        InsertTable.setString(2, socialSecurity);

        InsertTable.executeUpdate();

        return null;
    }

    //Inserting into person info
    public String personInfo(String name, String job, String phoneNumber, String zipcode, String buildingNumber, String streetName, String creditCard) throws SQLException{
        //Person info

        PreparedStatement InsertTable = connect.prepareStatement("INSERT INTO personInfo(PersonName, Job, PhoneNumber, Zipcode, BuildingNumber, StreetName, CreditCard)" +
                "VALUES(?,?,?,?,?,?,?)");

        InsertTable.setString(1, name);
        InsertTable.setString(2, job);
        InsertTable.setString(3, phoneNumber);
        InsertTable.setString(4, zipcode);
        InsertTable.setString(5, buildingNumber);
        InsertTable.setString(6, streetName);
        InsertTable.setString(7, creditCard);

        InsertTable.executeUpdate();

        return null;
    }

    //Zipcode and city insert
    public String zipCity(String zipcode, String city) throws SQLException{
        PreparedStatement InsertTable = connect.prepareStatement("INSERT INTO zipCity(Zipcode, City)" +
                "VALUES(?,?)");
        InsertTable.setString(1, zipcode);
        InsertTable.setString(2, city);

        InsertTable.executeUpdate();
        return null;
    }

    //City and state
    public String cityInfo(String city, String state) throws SQLException{
        PreparedStatement InsertTable = connect.prepareStatement("INSERT INTO cityInfo(City, State)" +
                "VALUES(?,?)");
        InsertTable.setString(1, city);
        InsertTable.setString(2, state);

        InsertTable.executeUpdate();

        return null;
    }

    //Credit Card number and company.
    public String creditInfo(String creditcard, String creditcardprovider) throws SQLException{
        PreparedStatement InsertTable = connect.prepareStatement("INSERT INTO creditCardInfoCompany(CreditCard, CreditCardProvider)" +
                "VALUES(?,?)");
        InsertTable.setString(1, creditcard);
        InsertTable.setString(2, creditcardprovider);

        InsertTable.executeUpdate();

        return null;
    }





    //Prints the tables
    public void PrintTables() throws SQLException{

        PreparedStatement testCompositeKey = connect.prepareStatement("SELECT * FROM ssnPersonKey");
        ResultSet resultsTest = testCompositeKey.executeQuery();
        SQLDatabaseConnection.print(resultsTest);

        PreparedStatement testPersonInfo = connect.prepareStatement("SELECT * FROM personInfo");
        ResultSet resultsPersonTest = testPersonInfo.executeQuery();
        SQLDatabaseConnection.print(resultsPersonTest);

        PreparedStatement testZipCity = connect.prepareStatement("SELECT * FROM zipCity");
        ResultSet resultsZipCity = testZipCity.executeQuery();
        SQLDatabaseConnection.print(resultsZipCity);

        PreparedStatement testCityInfo = connect.prepareStatement("SELECT * FROM cityInfo");
        ResultSet resultsCityInfo = testCityInfo.executeQuery();
        SQLDatabaseConnection.print(resultsCityInfo);

        PreparedStatement testCreditInfo = connect.prepareStatement("SELECT * FROM creditCardInfoCompany");
        ResultSet resultsCreditInfo = testCreditInfo.executeQuery();
        SQLDatabaseConnection.print(resultsCreditInfo);

        //Closes the tables once opened.
        testCompositeKey.close();
        testPersonInfo.close();
        testZipCity.close();
        testCityInfo.close();
        testCreditInfo.close();



    }
}
