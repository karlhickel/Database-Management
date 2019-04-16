
import java.io.IOException;
import java.sql.SQLException;
import java.sql.*;


public class Main {
    public static void main(String[] args) throws SQLException, IOException {
        Connection connect = SQLDatabaseConnection.getdatabaseconnection();


        //Creates tables
        DataBaseNormalizer tableCreation = new DataBaseNormalizer();
        tableCreation.TableCreation();


        //Reads CSVReader file

        CSVReader inputTable = new CSVReader();
        inputTable.FileReader();

        //Prints tables that have been created and have data inside.
        tableCreation.PrintTables();

        connect.close();



    }


}




