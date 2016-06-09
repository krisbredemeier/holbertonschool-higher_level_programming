//
//  ViewController.swift
//  Views 101
//
//  Created by Kristine Bredemeier on 6/9/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import UIKit

class ViewController: UIViewController {


    @IBOutlet weak var clockLabel: UILabel!
    let clock = Clock()
    var timer: NSTimer?

    override func viewDidLoad() {
        super.viewDidLoad()

        timer = NSTimer.scheduledTimerWithTimeInterval(1.0, target: self, selector: "updateTimeLabel", userInfo: nil, repeats: true)


    }

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        updateTimeLabel()
    }

    func updateTimeLabel() {
        let formatter = NSDateFormatter()
        formatter.timeStyle = .MediumStyle
        clockLabel.text = formatter.stringFromDate(clock.currentTime)
    }

    override func supportedInterfaceOrientations() -> UIInterfaceOrientationMask {
        return UIInterfaceOrientationMask.All
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    deinit {
        if let timer = self.timer {
            timer.invalidate()
        }
    }

}


