using System;
using System.Windows;
using System.Speech.Recognition;

namespace Speech_Recognition
{
    public partial class Window1 : System.Windows.Window
    {
        public Window1()
        {
            InitializeComponent();

            SpeechRecognizer recognizer = new SpeechRecognizer();
            GrammarBuilder builder = new GrammarBuilder();
            builder.Append(new Choices("two", "three", "four", "five", "six", "seven",
              "eight", "nine", "ten", "jack", "queen", "king", "ace"));
            builder.Append("of", 0, 1);
            builder.Append(new Choices("clubs", "diamonds", "spades", "hearts"));
            recognizer.LoadGrammar(new Grammar(builder));

            recognizer.SpeechRecognized +=
                new EventHandler<SpeechRecognizedEventArgs>(recognizer_SpeechRecognized);
        }

        void recognizer_SpeechRecognized(object sender, SpeechRecognizedEventArgs e)
        {
            MessageBox.Show("You said: " + e.Result.Text);
        }
    }
}