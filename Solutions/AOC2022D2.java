import java.io.File;
import java.io.FileNotFoundException;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Scanner;

public class AOC2022D2 {
    public static void main(String[] args) {

        ArrayList<String> fileData = getFileData("src/InputFile2");
        int score = 0;
        for (int i = 0; i < fileData.size(); i++) {
            if (fileData.get(i).startsWith("A")) {
                if (fileData.get(i).endsWith("Y")) {
                    score += 8;
                }
                if (fileData.get(i).endsWith("X")) {
                    score += 4;
                }
                if (fileData.get(i).endsWith("Z")) {
                    score += 3;
                }
            }
            if (fileData.get(i).startsWith("B")) {
                if (fileData.get(i).endsWith("Y")) {
                    score += 5;
                }
                if (fileData.get(i).endsWith("X")) {
                    score += 1;
                }
                if (fileData.get(i).endsWith("Z")) {
                    score += 9;
                }
            }
            if (fileData.get(i).startsWith("C")) {
                if (fileData.get(i).endsWith("Y")) {
                    score += 2;
                }
                if (fileData.get(i).endsWith("X")) {
                    score += 7;
                }
                if (fileData.get(i).endsWith("Z")) {
                    score += 6;
                }
            }
        }
        System.out.println("Part One: " + score);


        score = 0;
        for (int r= 0; r < fileData.size(); r++)
        {
            if (fileData.get(r).endsWith("Y"))
            {
                if (fileData.get(r).startsWith("C"))
                {
                    score += 6;
                }
                if (fileData.get(r).startsWith("B"))
                {
                    score += 5;
                }
                if (fileData.get(r).startsWith("A"))
                {
                    score += 4;
                }
            }
            if (fileData.get(r).endsWith("X"))
            {
                if (fileData.get(r).startsWith("C"))
                {
                    score += 2;
                }
                if (fileData.get(r).startsWith("B"))
                {
                    score += 1;
                }
                if (fileData.get(r).startsWith("A"))
                {
                    score += 3;
                }
            }
            if (fileData.get(r).endsWith("Z"))
            {
                if (fileData.get(r).startsWith("C"))
                {
                    score += 7;
                }
                if (fileData.get(r).startsWith("B"))
                {
                    score += 9;
                }
                if (fileData.get(r).startsWith("A"))
                {
                    score += 8;
                }
            }
        }
        System.out.println("Part Two: " + score);
        // you now have a list of Strings from the file "InputFile"
    }


    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                if (!line.equals(""))
                    fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }
}