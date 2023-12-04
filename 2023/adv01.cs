using System.Text;
using System.Text.RegularExpressions;

Dictionary<string, string> numbers = new()
{
    { "one", "1" },
    { "two", "2" },
    { "three", "3" },
    { "four", "4" },
    { "five", "5" },
    { "six", "6" },
    { "seven", "7" },
    { "eight", "8" },
    { "nine", "9" },
    { "zero", "0" }
};

const int BufferSize = 128;
using (var fileStream = File.OpenRead("adv01.txt"))
{
    Regex regexP1 = new(@"\d");
    Regex regexP2 = new(@"(one|two|three|four|five|six|seven|eight|nine|zero|\d)");

    using var streamReader = new StreamReader(fileStream, Encoding.UTF8, true, BufferSize);

    string? line;
    int sumP1 = 0, sumP2 = 0;
    while ((line = streamReader.ReadLine()) != null)
    {
        List<string> findListP1 = [], findListP2 = [];

        findListP1.AddRange(regexP1.Matches(line).Select(match => match.Value));

        for (int i = 0; i < line.Length; ++i)
        {
            Match match = regexP2.Match(line[i..]);

            if (match.Success)
                findListP2.Add(numbers.TryGetValue(match.Value, out var val) ? val : match.Value);
        }

        if (numbers.TryGetValue(findListP2[0], out var value))
            findListP2[0] = value;

        if (numbers.TryGetValue(findListP2[^1], out value))
            findListP2[^1] = value;

        sumP1 += int.Parse(findListP1[0] + findListP1[^1]);
        sumP2 += int.Parse(findListP2[0] + findListP2[^1]);
    }

    Console.WriteLine($"Part 1: {sumP1}");
    Console.WriteLine($"Part 2: {sumP2}");
}
