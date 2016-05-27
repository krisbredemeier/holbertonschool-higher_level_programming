//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//
//  Created by Kristine Bredemeier on 5/27/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import Foundation

class TechCompaniesHelper {

    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]

    init() {

    }


    static func getTechCompanies() -> [String] {
        return companies
    }

}