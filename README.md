# DSO138mini Web Plotter

An interactive web visualizer for the DSO138mini oscilloscope, allowing you to capture, analyze, and export signal data directly from your browser.

> ⚡ **Disclaimer**: This project was **vibe-coded** (developed experimentally and improvised, without formal planning). Use at your own risk!

## 🎯 Features

### Data Visualization
- **Time Mode**: View signals in time domain with configurable grid
- **FFT Mode**: Spectral analysis with multiple window options (Hann, Rectangular)
- **Zoom and Pan**: Full control over visualization with mouse wheel and dragging
- **Configurable Trigger**: Set trigger levels for better signal capture

### Measurements
- **Time Cursors**: Measure time differences (Δt) and frequency (1/Δt)
- **Voltage Cursors**: Measure voltage differences (ΔV)
- **Measurements Panel**: Automatic signal parameter reading (frequency, amplitude, RMS, etc.)

### Export
- **CSV**: Export raw data in CSV format for analysis in other tools
- **PNG**: Capture current visualization (Time or FFT) as image

### Auxiliary Tools
- **Serial Log**: Monitor all lines received from serial in real-time
- **Offline Mode**: Test the parser with example data without needing device connected
- **Shortcut Buttons**: Auto-scale, Reset zoom, Fit X/Y

## 🚀 Getting Started

### Hardware Setup

To use this plotter, you need to connect your **DSO138mini** to your PC via USB:

1. **Connect UART to USB**: 
   - Connect the DSO138mini's **TX** pin to the USB-UART adapter's **RX** pin
   - Connect the DSO138mini's **RX** pin to the USB-UART adapter's **TX** pin
   - Connect **GND** to **GND**
   - Use a USB-to-UART converter (FT232RL, CH340, etc.) connected to your PC

2. **Baud Rate**: 115200 bps (pre-configured)

3. **Send Data to PC**:
   - On the DSO138mini, **hold the SELECT button for 3 seconds**
   - The device will dump the current waveform data via serial
   - The plotter will automatically receive and display it

### Start the Server

The Web Serial API only works on HTTPS or localhost, so you must run this locally:

#### Windows
1. Make sure **Python 3** is installed
2. Double-click **`run.bat`** (server will start automatically)
3. Your browser will open to `http://localhost:8000`

#### macOS / Linux
```bash
python3 server.py
```
Then open `http://localhost:8000/index.html` in your browser

#### Manual (Any OS)
```bash
python3 -m http.server 8000
```
Then open `http://localhost:8000/index.html` in your browser

⚠️ **Important**: Do NOT open directly as `file://` - Web Serial API won't work!

### Connect to Device

1. Server is already running on `http://localhost:8000` (previous step)
2. Click the **"Connect"** button in the top right
3. Select the serial port corresponding to your DSO138mini USB adapter
4. Connection indicator will turn green when connected
5. On the DSO138mini: **Hold SELECT button for 3 seconds** to send data dump
6. Waveform will automatically appear and update

### Using the Plotter

#### Display Modes
- **Time Tab**: Standard waveform visualization with time domain
- **FFT Tab**: Frequency spectrum analysis in dB scale

#### Using Cursors (Time Mode)

1. Open the **Settings** panel (click "MENU" on the right)
2. At the bottom, enable:
   - **Cursor T (Δt)**: To measure time differences
   - **Cursor V (ΔV)**: To measure voltage differences
3. Drag the cursors over the graph to position them
4. Measurements update automatically

#### Measurements Panel

- Click the 📏 icon (top right) to open measurements panel
- Displays automatically: frequency, amplitude, Vrms, Vmax, Vmin, duty cycle
- Panel updates in real-time as you move cursors

#### Export Data

1. Open **Settings** panel (MENU)
2. **Export** section:
   - **Save CSV**: Export raw data and metadata
   - **Save PNG**: Capture current view as image

#### Test Without Device

1. Open **Settings** panel (MENU)
2. **Test Without Serial (Parser)** section
3. Paste data from a DSO138 dump or click **"Load Example"**
4. Click **"Parse"** to process the data

## 🎮 Controls

| Action | Control |
|--------|----------|
| Zoom | Mouse wheel |
| Zoom Y (Voltage) | `Shift` + Mouse wheel |
| Pan (Move) | Click and drag background |
| Move Cursors | Click and drag cursors directly |
| Auto-scale | "Auto" button |
| Reset Zoom | "Reset" button |
| Fit X axis | "Fit X" button |
| Fit Y axis | "Fit Y" button |

## ⚙️ Settings

### Visual
- **Grid**: Toggle reference grid on/off
- **Trigger (V)**: Set signal trigger level
- **FFT Window**: Choose between Hann or Rectangular window for spectral analysis

### Capture
- **Clear Capture**: Remove all captured data and reset visualization

## 📋 Requirements

- Modern browser with Web Serial API support (Chrome, Edge, Chromium-based)
- DSO138mini oscilloscope
- USB-to-UART converter (FT232RL, CH340, etc.)
- Python 3 (for running the local server)

## 🔧 Built With

- **HTML5 Canvas**: For graph rendering
- **Web Serial API**: For device communication
- **Pure JavaScript**: No external dependencies
- **Responsive Design**: Works on different screen sizes

## 📝 Notes

- The plotter keeps up to 2500 lines of log history to prevent memory issues
- Data is processed in real-time as received
- Interface is optimized for desktop but works on tablets

## 💡 Tips

- Use the **Serial Log** to diagnose communication issues
- Try **Offline Mode** to test features without device connected
- Combine **cursors** and **measurements** for precise analysis
- Export to **PNG** to document your measurements
- Adjust **trigger level** to stabilize periodic signals

## 📁 Project Structure

```
.
├── index.html        (Main web interface - start here)
├── server.py         (Python HTTP server)
├── run.bat           (Windows launcher)
└── README.md         (This file)
```

## 🎨 About This Project

This is a **vibe-coded** project - developed experimentally and improvised, without formal planning or extensive documentation. The code works, but may have:

- Creative and unconventional solutions
- Limited edge case coverage
- Informal code style
- Features implemented quickly

**Use at your own risk!** Contributions and improvements are welcome.

---

**DSO138mini Web Plotter** - Developed to make signal analysis and visualization from the DSO138mini oscilloscope easier and more accessible.
