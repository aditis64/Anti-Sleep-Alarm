<header>
    <h1>AI-Based Drowsy Driving Detection System</h1>
</header>

<section>
    <h2>Overview</h2>
    <p>This project aims to reduce accidents caused by drowsy driving by detecting signs of fatigue in drivers and taking corrective actions. It uses facial recognition to monitor the driver’s eyes for signs of drowsiness, providing voice alerts, activating alarms, and gradually applying the vehicle’s brakes if the driver remains unresponsive.</p>
</section>

<section>
    <h2>Features</h2>
    <ul>
        <li><strong>Drowsiness Detection</strong>: Monitors the driver’s face and eyes for lack of movement or blinking.</li>
        <li><strong>Voice Alerts</strong>: Warns the driver with voice prompts (e.g., "Driver, you're sleepy").</li>
        <li><strong>Alarm & Braking</strong>: Triggers an alarm and applies gradual braking if the driver doesn't respond.</li>
        <li><strong>Affordable & Easy Setup</strong>: Simple installation and low-cost components.</li>
    </ul>
</section>

<section>
    <h2>Motivation</h2>
    <p>Driver fatigue is a major cause of traffic accidents, particularly for long-haul truck drivers. This system aims to prevent these accidents by using AI to detect drowsiness and ensure driver safety.</p>
</section>

<section>
    <h2>Requirements</h2>
    <ul>
        <li><strong>Hardware:</strong>
            <ul>
                <li>Raspberry Pi</li>
                <li>IR Camera (for face detection)</li>
                <li>Buzzer and LED (for alerts)</li>
                <li>Motor driver for emergency braking</li>
            </ul>
        </li>
        <li><strong>Software:</strong>
            <ul>
                <li>Python 3.x</li>
                <li>Libraries: <code>OpenCV</code>, <code>face_recognition</code>, <code>espeak</code>, <code>RPi.GPIO</code>, <code>gpiozero</code></li>
            </ul>
        </li>
    </ul>
</section>

<section>
    <h2>How It Works</h2>
    <p>The system detects the driver’s face and eyes, then checks for signs of drowsiness. If detected, the system triggers a voice alert, followed by an alarm and eventual braking if unresponsive.</p>
</section>

<section>
    <h2>Results</h2>
    <ul>
        <li>Successfully detects drowsiness through facial recognition and eye movement analysis.</li>
        <li>Provides voice alerts and visual cues (LED) to warn the driver.</li>
        <li>If unresponsive, activates an alarm and gradually applies brakes to stop the vehicle.</li>
    </ul>
</section>

<footer>
  
  And the review link: https://drive.google.com/file/d/1TCcw79pgj4U-xQWvUOtaLdk5ZdDALp8i/view?usp=sharing
</footer>
    
