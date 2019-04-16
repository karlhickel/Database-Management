import com.mysql.cj.mysqlx.protobuf.MysqlxCrud;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;


public class CSVReader {

    Connection connect = SQLDatabaseConnection.getdatabaseconnection();

    private static final String csvFilePath = "/Users/karlhickel/Desktop/out.csv";

    DataBaseNormalizer testInsert = new DataBaseNormalizer();

    public String name;
    public String job;
    public String phoneNumber;
    public String state;
    public String zipcode;
    public String streetName;
    public String buildingNumber;
    public String city;
    public String creditCard;
    public String creditProvider;
    public String socialSecurityNumber;



    public void FileReader() throws IOException {

        try (
                Reader reader = Files.newBufferedReader(Paths.get(csvFilePath));
                CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT);
        ) {
            for (CSVRecord csvRecord : csvParser) {
                // Accessing Values by Column Index
                name = csvRecord.get(0);
                job = csvRecord.get(1);
                phoneNumber = csvRecord.get(2);
                state = csvRecord.get(3);
                zipcode = csvRecord.get(4);
                streetName = csvRecord.get(5);
                buildingNumber = csvRecord.get(6);
                city = csvRecord.get(7);
                creditCard = csvRecord.get(8);
                creditProvider = csvRecord.get(9);
                socialSecurityNumber = csvRecord.get(10);

                //Inserts into person key
                testInsert.ssnPersonKey(name, socialSecurityNumber);

                //Inserts into the personinfo
                testInsert.personInfo(name, job, phoneNumber, zipcode, buildingNumber, streetName, creditCard);

                //Inserts into the zipcode city
                testInsert.zipCity(zipcode, city);

                //Inserts into the city info
                testInsert.cityInfo(city, state);

                //Inserts into creditInfo
                testInsert.creditInfo(creditCard,creditProvider);



                //Prints out records that are being inputed into a table.
                System.out.println("Record No - " + csvRecord.getRecordNumber());
                System.out.println("---------------");
                System.out.println("Name : " + name);
                System.out.println("Job : " + job);
                System.out.println("Phone Number : " + phoneNumber);
                System.out.println("State : " + state);
                System.out.println("Zipcode : " + zipcode);
                System.out.println("Street Name : " + streetName);
                System.out.println("Building Number : " + buildingNumber);
                System.out.println("City : " + city);
                System.out.println("Credit Card : " + creditCard);
                System.out.println("Credit Card Provider : " + creditProvider);
                System.out.println("Social Security Number : " + socialSecurityNumber);
                System.out.println("---------------\n\n");
            }
        }
        catch (SQLException e) {
            e.printStackTrace();
        }

    }
}


