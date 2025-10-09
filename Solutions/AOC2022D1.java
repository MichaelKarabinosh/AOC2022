import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class AOC2022D1 {
    public static void main(String[] args) {

        ArrayList<String> fileData = getFileData("src/InputFile1");
        // you now have a list of Strings from the file "InputFile"
        int runningTotal = 0;
        ArrayList<Integer> sizes = new ArrayList<>();
        for (int i = 0; i < fileData.size(); i++)
        {
            if (fileData.get(i).isEmpty())
            {
                sizes.add(runningTotal);
                runningTotal = 0;
            }
            else {
                runningTotal += Integer.parseInt(fileData.get(i));
            }
        }
      Collections.sort(sizes);
        System.out.println("Part One: " + sizes.getLast());
        int x = 0;
        for (int i = 0; i < 3; i++) {
            x += sizes.getLast();
            sizes.removeLast();
        }
        System.out.println("Part Two: " + x);
    }


    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }
}