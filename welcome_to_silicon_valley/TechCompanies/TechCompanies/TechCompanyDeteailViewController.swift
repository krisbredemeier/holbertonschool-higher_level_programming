//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Kristine Bredemeier on 5/27/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import UIKit

class TechCompanyDetailViewController: UIViewController {

    // connect lable and image

    var entity:Entity!


    @IBOutlet weak var lable_entity: UILabel!
    @IBOutlet weak var image_entity: UIImageView!



    //var label = UILabel(frame: CGectMake(10, 10, 200, 21))
    //    self.view.addSubView(label)

    override func viewDidLoad() {
        super.viewDidLoad()

        if self.entity != nil {

            self.title = entity.name
            self.lable_entity.text = entity.town
            self.image_entity.image = UIImage(imageLiteral: entity.imageName)
            self.image_entity.contentMode = .ScaleAspectFit
        }

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    


    // MARK: - Navigation


}
