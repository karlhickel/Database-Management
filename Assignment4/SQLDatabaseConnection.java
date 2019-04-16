import java.sql.*;


//Prints results of a database
public class SQLDatabaseConnection {
    static void print(ResultSet results) throws SQLException {
        ResultSetMetaData data = results.getMetaData();

        int numberOfColumns = data.getColumnCount();
        for (int i = 1; i<= numberOfColumns; i++) {
            if (i > 1) System.out.print(" ");
            String columnName = data.getColumnName(i);
            System.out.print(columnName);
        }

        System.out.println();

        while (results.next()) {
            for (int i = 1; i <= numberOfColumns; i++) {
                if (i > 1) System.out.print(" ");
                String columnValue = results.getString(i);
                System.out.print(columnValue);
            }
            System.out.println();
        }

    }


    //Connects to a database
    static Connection getdatabaseconnection()

    {
        try {
            return DriverManager.getConnection("jdbc:mysql://35.185.249.137:3306/cpsc408?useSSL=false","test",
                    "password" );
        }
        catch (SQLException e) {
            e.printStackTrace();
        }

        return null;
    }


//?useSSL=false

}
