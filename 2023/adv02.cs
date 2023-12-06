using System.Text;
using System.Text.RegularExpressions;

const int BufferSize = 128;
Dictionary<string, int> maxBalls = new() {
    { "red", 12 },
    { "green", 13 },
    { "blue", 14  }
};

using (var fileStream = File.OpenRead("adv02.txt"))
{
    Regex regexNumber = new(@"\d+");
    using var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize);

    string? line;
    int sumP1 = 0, sumP2 = 0;
    while ((line = streamReader.ReadLine()) != null)
    {
        string[] parts = line.Split(": ");
        string[] games = parts[1].Split(";");
        bool shouldCountGame = true;

        int maxRed = 1;
        int maxGreen = 1;
        int maxBlue = 1;

        foreach (string game in games)
        {
            string[] results = game.Split(", ");

            foreach (string result in results)
            {
                string[] resultSplits = result.Trim().Split(" ");
                int balls = int.Parse(resultSplits[0]);

                if (balls > maxBalls[resultSplits[1]])
                    shouldCountGame = false;

                if (resultSplits[1] == "red")
                    maxRed = Math.Max(maxRed, balls);
                else if (resultSplits[1] == "green")
                    maxGreen = Math.Max(maxGreen, balls);
                else if (resultSplits[1] == "blue")
                    maxBlue = Math.Max(maxBlue, balls);
            }
        }

        if (shouldCountGame)
            sumP1 += int.Parse(regexNumber.Match(parts[0]).Value);

        sumP2 += maxRed * maxGreen * maxBlue;
    }

    Console.WriteLine($"Part 1: {sumP1}");
    Console.WriteLine($"Part 2: {sumP2}");
}