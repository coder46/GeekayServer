﻿

#pragma checksum "C:\Users\faisal\Desktop\GeekayGames\BasicCapturing\BasicCapturing\PhoneJupiter\..\UniversalJupiter\UniversalJupiter.Shared\VideoCapturePage.xaml" "{406ea660-64cf-4c82-b6f0-42d48172a799}" "BB4917063C95C2178894BA2A95A076C8"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace UniversalJupiter
{
    partial class VideoCapturePage : global::Windows.UI.Xaml.Controls.Page, global::Windows.UI.Xaml.Markup.IComponentConnector
    {
        [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.Windows.UI.Xaml.Build.Tasks"," 4.0.0.0")]
        [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
 
        public void Connect(int connectionId, object target)
        {
            switch(connectionId)
            {
            case 1:
                #line 20 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.MediaElement)(target)).MediaEnded += this.PlaybackElement_MediaEnded;
                 #line default
                 #line hidden
                break;
            case 2:
                #line 21 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.Primitives.ButtonBase)(target)).Click += this.BtnRecordVideo_Click;
                 #line default
                 #line hidden
                break;
            case 3:
                #line 24 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.Primitives.RangeBase)(target)).ValueChanged += this.SliderBrightness_ValueChanged;
                 #line default
                 #line hidden
                break;
            case 4:
                #line 26 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.Primitives.RangeBase)(target)).ValueChanged += this.SliderFocus_ValueChanged;
                 #line default
                 #line hidden
                break;
            case 5:
                #line 28 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.Primitives.RangeBase)(target)).ValueChanged += this.SliderZoom_ValueChanged;
                 #line default
                 #line hidden
                break;
            case 6:
                #line 30 "..\..\VideoCapturePage.xaml"
                ((global::Windows.UI.Xaml.Controls.Primitives.RangeBase)(target)).ValueChanged += this.SliderHue_ValueChanged;
                 #line default
                 #line hidden
                break;
            }
            this._contentLoaded = true;
        }
    }
}


